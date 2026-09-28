from book_manager.ui.console import ConsolaUI


def main(import_default_data=False):
    app = ConsolaUI()
    app.iniciar()


if __name__ == "__main__":
    main()
    
###ejecutar main copiar y pegar  >>>>  python -m book_manager.main  <<<