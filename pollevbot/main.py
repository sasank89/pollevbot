from pollevbot import PollBot


def main():
    user = 'madhurya.amirapu@stvincenthospital.com'
    password = 'My Password'
    host = 'sasankkalipatnapu152'
    login_type = 'pollev'

    # If you're using a non-uw PollEv account,
    # add the argument "login_type='pollev'"
    with PollBot(user, password, host) as bot:
        bot.run()


if __name__ == '__main__':
    main()
