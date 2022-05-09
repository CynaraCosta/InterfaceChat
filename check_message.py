from datetime import datetime

def is_valid_to_send(text, nickname):
    if text.replace(" ", '') == '':
            return "Favor digite uma mensagem válida antes de enviar!"

    time_now = datetime.now()
    return f'< {time_now.strftime("%H:%M")} {nickname}: > {text}'

def is_valid_to_print(message_received):
    if message_received == "Favor digite uma mensagem válida antes de enviar!":
        return False