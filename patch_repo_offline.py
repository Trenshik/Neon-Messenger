import re

with open("app/src/main/java/com/example/data/AppDatabase.kt", "r") as f:
    content = f.read()

message_dao_update = """    @Query("UPDATE messages SET isDelivered = :isDelivered WHERE id = :messageId")
    suspend fun updateMessageDelivery(messageId: String, isDelivered: Boolean)"""

content = content.replace('    @Query("UPDATE messages SET isRead = 1 WHERE chatId = :chatId AND senderId != :myUserId")', message_dao_update + '\n    @Query("UPDATE messages SET isRead = 1 WHERE chatId = :chatId AND senderId != :myUserId")')

repo_update = """    suspend fun updateMessageDelivery(messageId: String, isDelivered: Boolean) = messageDao.updateMessageDelivery(messageId, isDelivered)"""

content = content.replace('    suspend fun markAsRead(chatId: String, myUserId: String) = messageDao.markAsRead(chatId, myUserId)', repo_update + '\n    suspend fun markAsRead(chatId: String, myUserId: String) = messageDao.markAsRead(chatId, myUserId)')

with open("app/src/main/java/com/example/data/AppDatabase.kt", "w") as f:
    f.write(content)

