"""
    Format docstring to be able to entry in DeepL or GoogleTranslate

    You can try this function in main() at near bottom of this code.
"""

OUTPUT_TXT: str = ''


def docstring_formatter(name_obj: object,
                        times_red: int = 2,
                        rmv_t: bool = True,
                        rmv_n: bool = True) -> str:
    """
    Format docstring to be able to entry in DeepL or GoogleTranslate etc.

        Main function:
         1. Remove indent
         2. Reduce extra spaces

         :param name_obj: name of object which has docstring
         :param times_red: how times to repeat space reducing
         :param rmv_t: True is needed to remove '\\t' and True is default
         :param rmv_n: True is needed to remove '\\n' and True is default
         :return: formatted docstring as str_type
    """

    def space_reducer(s: str, n_repeat: int = times_red) -> str:
        """
        Reduce 2 spaces to 1 space.

         :param s: strings received
         :param n_repeat: how times to repeat space reducing
         :return: strings formatted
        """
        for _ in range(n_repeat):
            s = s.replace('  ', ' ')
        return s

    def remover(s: str, escape: str = '') -> str:
        """
        Remove escape sequence indicated to remove.

        :param s: strings received
        :param escape: escape sequence to remove
        :return: strings formatted
        """
        return s.replace(escape, '')

    docstr = str(name_obj.__doc__)
    global OUTPUT_TXT

    if rmv_t:
        docstr = remover(docstr, escape='\t')
    if rmv_n:
        docstr = remover(docstr, escape='\n')
    if times_red:
        docstr = OUTPUT_TXT = space_reducer(docstr)
        return docstr
    else:
        OUTPUT_TXT = docstr
        return docstr


def console_constructor(str1: str, str2: str):
    """Form console display"""
    print('■' * 120)
    print('   Formatted Sentence   ')
    print('━' * 120)
    print(str1, end='\n\n')
    print('■' * 120)
    print('   Original Sentence   ')
    print('━' * 120)
    print(str2)


def txt_outputter(output: bool = False, filename: str = 'docstring_formatted'):
    """
    Output process result as a txt file.
    
    :param output: whether textfile output or not
    :param filename: filename strings without filename extension, for example, '.txt'
    """
    f_name = filename + '.txt'
    global OUTPUT_TXT
    if output:
        with open(f_name, 'w') as txtfile:
            txtfile.write(OUTPUT_TXT)


def main():
    """
    You can try the function here.
    """

    # If the object requires import of module, you do so like the under example 'logging'
    import logging
    # Assign the identifier of object to 'name_object'
    name_object = logging.Logger
    # Default Setting at main() --> name_obj=name_object, times_red=2, rmv_t=True, rmv_n=True
    str_result = docstring_formatter(name_obj=name_object, times_red=2, rmv_t=True, rmv_n=True)

    console_constructor(str_result, name_object.__doc__)

    # If you need the output txt-file, revalue the 'output' arg to True.
    # You can change the output file name by rewriting 'filename' arg.
    txt_outputter(output=False, filename='docstring_formatted')

    # When you want the output is the same as 'Original Sentence' displayed on console,
    # revalue the arguments setting of docstring_formatter() like below.
    #
    # Setting at main() --> name_obj=name_object, times_red=0, rmv_t=False, rmv_n=False


if __name__ == '__main__':
    main()
