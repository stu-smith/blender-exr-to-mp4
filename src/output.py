import colorama

colorama.init()

RESET = colorama.Style.RESET_ALL


class Output(object):

    @staticmethod
    def info(msg):
        print(msg)

    @staticmethod
    def checkpoint(msg):
        style = colorama.Fore.GREEN
        print(style + msg + RESET)

    @staticmethod
    def fatal(msg):
        style = colorama.Fore.RED + colorama.Style.BRIGHT
        print('')
        print(style + msg + RESET)
        print('')
        print('Exiting with failure...')
        exit(1)

    @staticmethod
    def title(msg):
        style = colorama.Fore.CYAN + colorama.Style.BRIGHT
        print('')
        print('')
        print(style + msg + RESET)
        print('=' * 80)
        print('')
