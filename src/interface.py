from .sql import session, Pessoa
import gi


gi.require_version('Gtk', '3.0')


from gi.repository import Gtk


class App:
    def __init__(self):
        self.builder = Gtk.Builder()

        # obtendo a interface glade.
        self.builder.add_from_file('interface.glade')

        # obtendo objetos.
        self.janela = self.builder.get_object('janela')
        self.botao_gravar = self.builder.get_object('gravar')
        self.entrada_nome = self.builder.get_object('nome')
        self.entrada_idade = self.builder.get_object('idade')
        self.entrada_cpf = self.builder.get_object('cpf')
        self.treeview = self.builder.get_object('treeview')

        # criando objetos
        self.liststore = Gtk.ListStore(str, int, int)
        renderText = Gtk.CellRendererText()
        renderText2 = Gtk.CellRendererText()
        renderText3 = Gtk.CellRendererText()
        coluna = Gtk.TreeViewColumn("nome", renderText, text=0)
        coluna2 = Gtk.TreeViewColumn("idade", renderText2, text=1)
        coluna3 = Gtk.TreeViewColumn("cpf", renderText3, text=2)
        self.treeview.append_column(coluna)
        self.treeview.append_column(coluna2)
        self.treeview.append_column(coluna3)
        self.treeview.set_model(self.liststore)


        # conectando objetos.
        self.janela.connect('destroy', Gtk.main_quit)
        self.botao_gravar.connect('clicked', self.gravar_clicado)

        # configurando.
        self.janela.show_all()
        self.exibir()


    def limpar_entradas(self):
        self.entrada_nome.set_text('')
        self.entrada_idade.set_text('')
        self.entrada_cpf.set_text('')

    def gravar_clicado(self, botao):
        nome = self.entrada_nome.get_text()
        idade = self.entrada_idade.get_text()
        cpf = self.entrada_cpf.get_text()
        if all([nome, idade, cpf]):
            pessoa = Pessoa(nome=nome, idade=idade, cpf=cpf)
            session.add(pessoa)
            session.commit()
        self.limpar_entradas()
        self.liststore.clear()
        self.exibir()

    def exibir(self):
        pessoas = session.query(Pessoa).all()
        for pessoa in pessoas:
            self.liststore.append(
                [pessoa.nome, pessoa.idade, pessoa.cpf]
            )
