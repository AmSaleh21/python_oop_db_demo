import re


def email_checker(email):
    regex = re.compile(r"\b[\w-]+@[\w-]+\.\w{2,4}\b")

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def format_email(sender, to, sub, receiver_name, body):
    return f'''
            from:{sender}
            to:{to}
            
            subject:{sub}

            Dear {receiver_name},

            \t{body}

            \tBestRegards 
    '''


def write_email(email):
    file = open('email', 'w')
    file.write(email)
    file.close()
