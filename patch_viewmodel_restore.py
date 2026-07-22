import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

restored_methods = """
    fun markMessagesAsRead(chatId: String, myUserId: String) {
        viewModelScope.launch {
            repository.markAsRead(chatId, myUserId)
        }
    }
    fun saveDraft(chatId: String, text: String?) {
        viewModelScope.launch {
            repository.updateDraft(chatId, text)
        }
    }
    fun addReaction(messageId: String, reaction: String) {
        viewModelScope.launch {
            repository.updateReaction(messageId, reaction)
        }
    }
    fun pinMessage(messageId: String) {
        viewModelScope.launch {
            repository.updatePinStatus(messageId, true)
        }
    }
    fun unpinMessage(messageId: String) {
        viewModelScope.launch {
            repository.updatePinStatus(messageId, false)
        }
    }
    fun switchAccount(accountId: String) {
        viewModelScope.launch {
            repository.switchActiveAccount(accountId)
        }
    }
    fun createAccount(username: String, displayName: String, bio: String = "", profilePicUrl: String = "", customStatus: String = "") {
        viewModelScope.launch {
            val account = UserAccount(
                id = java.util.UUID.randomUUID().toString(),
                username = username,
                displayName = displayName,
                bio = bio,
                profilePicUrl = profilePicUrl,
                customStatus = customStatus,
                isActive = true
            )
            repository.logoutAll()
            repository.insertAccount(account)
        }
    }
    fun addAccountAction() {
        _isAddingAccount.value = true
    }
    fun verify2FA(accountId: String, code: String) {
        _requires2FA.value = null
    }
    fun cancel2FA() {
        _requires2FA.value = null
    }
    fun createSecretChat(contactId: String) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), name = "Secret Chat", isGroup = false, isSecret = true)
            repository.insertChat(chat)
        }
    }
    fun createChat(name: String, isGroup: Boolean = false, isSecret: Boolean = false, isChannel: Boolean = false) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), name = name, isGroup = isGroup, isSecret = isSecret, isChannel = isChannel)
            repository.insertChat(chat)
        }
    }
    fun toggleArchive(chatId: String) {
        viewModelScope.launch {
            val chat = repository.allChats.firstOrNull()?.find { it.id == chatId }
            if (chat != null) {
                repository.updateArchiveStatus(chatId, !chat.isArchived)
            }
        }
    }
    fun setAutoThemeEnabled(enabled: Boolean) {
        _isAutoThemeEnabled.value = enabled
        repository.saveAutoThemeSwitcherEnabled(enabled)
    }
    fun setDarkThemeEnabled(enabled: Boolean) {
        _isDarkThemeEnabled.value = enabled
        repository.saveDarkThemeEnabled(enabled)
    }
    fun setBatterySaverEnabled(enabled: Boolean) {
        _batterySaverEnabled.value = enabled
        repository.saveBatterySaverEnabled(enabled)
    }
    fun setThemeOpacity(opacity: Float) {
        _themeOpacity.value = opacity
        repository.saveThemeOpacity(opacity)
    }
    fun setCustomPrimaryColor(color: Long?) {
        _customPrimaryColor.value = color
        if (color != null) repository.saveCustomPrimaryColor(color)
    }
    fun setCustomSecondaryColor(color: Long?) {
        _customSecondaryColor.value = color
        if (color != null) repository.saveCustomSecondaryColor(color)
    }
    fun switchTheme(theme: AppTheme) {
        _theme.value = theme
        repository.saveTheme(theme.name)
    }
    fun toggleFavoriteTheme(themeName: String) {
        val current = _favoriteThemes.value.toMutableSet()
        if (current.contains(themeName)) current.remove(themeName) else current.add(themeName)
        _favoriteThemes.value = current
        repository.saveFavoriteThemes(current)
    }
    fun importTheme(themeCode: String) {
        try {
            val parts = themeCode.substringAfter("Neon Messenger Theme Code: ").split("-")
            if (parts.size >= 3) {
                val themeName = parts[0]
                val primaryStr = parts[1]
                val secondaryStr = parts[2]
                switchTheme(AppTheme.valueOf(themeName))
                setCustomPrimaryColor(if (primaryStr != "def") primaryStr.toLongOrNull() else null)
                setCustomSecondaryColor(if (secondaryStr != "def") secondaryStr.toLongOrNull() else null)
                setAutoThemeEnabled(false)
            }
        } catch (e: Exception) {}
    }
    fun resetTheme() {
        switchTheme(AppTheme.DEFAULT)
        setCustomPrimaryColor(null)
        setCustomSecondaryColor(null)
        setAutoThemeEnabled(false)
    }
    fun logout() {
        viewModelScope.launch {
            repository.logoutAll()
        }
    }
    fun checkAutoTheme() {}
    fun addBot(chatId: String, botId: String, botName: String) {}
"""

# Insert before the last closing brace
content = content.strip()
if content.endswith("}"):
    content = content[:-1] + restored_methods + "\n}"

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "w") as f:
    f.write(content)
