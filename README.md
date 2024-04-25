# Monitoria de Introdução à Ciência de Dados 2024.1

Repositório para a Monitoria da disciplina de Introdução à Ciência de Dados 2024.1, aqui teremos um tutorial básico de html e css.

### Monitor
- [Sillas Rocha da Costa](https://www.github.com/scrocha)

## HTML Básico

O HTML (HyperText Markup Language) é a linguagem padrão para a criação de páginas da web. É composto por uma série de elementos que definem a estrutura e o conteúdo de uma página web.

### Estrutura Básica do HTML:

- `<!DOCTYPE html>`: Define o tipo de documento como HTML5.
- `<html>`: Define o início do documento HTML.
- `<head>`: Contém informações sobre o documento, como título, estilos e metadados.
- `<body>`: Contém o conteúdo visível do documento, como texto, imagens e links.

### Elementos Básicos de Texto:

- `<title>`: Define o título do documento exibido na barra de título do navegador.
- `<p>`: Define um parágrafo de texto.
- `<br>`: Cria uma quebra de linha.

#### Cabeçalhos:

Vão do `<h1></h1>` até o `<h6></h6>` e definem a ordem de importância dos cabeçalhos, sendo o `<h1>` o maior e mais importante.

### Inserção de Links e Imagens

Para inserir links e imagens em nosso HTML, usaremos `<a>` e `<img>`, respectivamente. É necessário adicionar atributos a esses elementos, como `href` para o link e `src` para a imagem, além de `width` e `height` se necessário para ajustar o tamanho da imagem.

Aqui está um exemplo básico de HTML:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Seu título aqui</title>
</head>

<body>

    <h1>Sua Heading aqui</h1>
    <p>Um parágrafo</p>

    <a href="https://www.exemplo.com">Link para exemplo.com</a>
    <br>
    <img src="caminho/para/sua/imagem.jpg" alt="Descrição da imagem" width="200" height="150">

</body>

</html> 
