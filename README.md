# AvitoParser

AvitoParser is an open-source project for scraping advertisements data from the Avito website. It provides a simple and efficient way to extract information from Avito listings and store it in a structured format.

## Installation

To use AvitoParser, you need to have Python installed on your system. The project uses Poetry as the package manager. Follow the steps below to set up the project:

Clone the repository:

```bash
git clone https://github.com/Sirius-Bell/avitoparser.git
```

Navigate to the project directory:

```bash
cd avitoparser
```

Install the dependencies using Poetry:

```bash
poetry install
```

This will create a virtual environment and install all the necessary packages.

## Usage

To use AvitoParser, you can refer to the avito.py file in the project. It contains an example of how to scrape data from the Avito website. You can modify the code according to your specific requirements.

Here's a basic example that demonstrates how to use AvitoParser:

```python
from avitoparser.avito import AvitoParser

# Instantiate the parser
parser = AvitoParser(driver="firefox")

parser.get_in_avito(parser.generate_search_url("buy room"))

# Scrape the data
adv = parser.parse()

# Process the data or save it to a file(csv supports)
# ...
```

## Contributing

Contributions to AvitoParser are welcome! If you find a bug or have a suggestion, please open an issue on the GitHub repository.

If you'd like to contribute code to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request on the main repository.

Please ensure that your code follows the project's coding style and is well-documented.

## License

AvitoParser is released under the GNU GENERAL PUBLIC LICENSE v3.0. Feel free to use, modify, and distribute the code for personal or commercial projects.