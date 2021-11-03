QUEUE = {}


def add_to_queue(chat_id, songname, ytlink, ref, type, url):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, ytlink, ref, type, url])
        return int(len(chat_queue) - 1)
    QUEUE[chat_id] = [[songname, ytlink, ref, type, url]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        return QUEUE[chat_id]
    return 0


def pop_an_item(chat_id):
    if chat_id not in QUEUE:
        return 0

    chat_queue = QUEUE[chat_id]
    chat_queue.pop(0)
    return 1


def clear_queue(chat_id: int):
    if chat_id not in QUEUE:
        return 0

    QUEUE.pop(chat_id)
    return 1
