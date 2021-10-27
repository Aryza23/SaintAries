import ast
from aries import REDIS

try:
    ast.literal_eval(REDIS.get("Approvals"))
except BaseException:
    REDIS.set("Approvals", "{}")


def approve(chat_id, user_id):
    approved = ast.literal_eval(REDIS.get("Approvals"))
    try:
        list = approved[chat_id]
        if user_id not in list:
            list.append(user_id)
        approved.update({chat_id: list})
    except BaseException:
        approved.update({chat_id: [user_id]})
    return REDIS.set("Approvals", str(approved))


def disapprove(chat_id, user_id):
    approved = ast.literal_eval(REDIS.get("Approvals"))
    try:
        list = approved[chat_id]
        if user_id in list:
            list.remove(user_id)
        approved.update({chat_id: list})
    except BaseException:
        pass
    return REDIS.set("Approvals", str(approved))


def is_approved(chat_id, user_id):
    approved = ast.literal_eval(REDIS.get("Approvals"))
    try:
        list = approved[chat_id]
        if user_id in list:
            return True
        return
    except BaseException:
        return


def list_approved(chat_id):
    approved = ast.literal_eval(REDIS.get("Approvals"))
    try:
        return approved[chat_id]
    except BaseException:
        return
