 # Static Site Generator

 A lightweight static site generator that converts Markdown content to HTML pages with customizable templates.

 ## Why?

 This project aims to solve the common problem of maintaining simple websites without relying on complex frameworks or content management systems. By using Markdown for content creation and HTML templates for styling, this static site generator provides:

 - Fast, secure, and lightweight website generation
 - Simple content management with Markdown files
 - Flexible templating system
 - GitHub Pages compatibility with configurable base paths
 - No database required, making deployment easy

 ## Quick Start

 1. Clone the repository:
    ```bash
    git clone https:github.com/yourusername/StaticSiteGenerator.git
    cd StaticSiteGenerator
    ```

 2. Create your content in Markdown format under the `content/` directory.

 3. Customize your template in `template.html`.

 4. Generate your site:
    ```bash
    python src/main.py
    ```

 5. Your site will be generated in the `docs/` directory.

 ## Usage

 ### Project Structure

 ```
 StaticSiteGenerator/
 ├── content/            # Markdown content files
 ├── static/             # Static assets (CSS, JS, images)
 ├── template.html       # HTML template
 ├── src/                # Source code
 └── docs/               # Generated site (output)
 ```

 ### Creating Content

 Create Markdown files in the `content/` directory. Each file should start with an H1 header that will be used as the page title:

 ```markdown
 # Page Title

 This is a paragraph with **bold** and _italic_ text.

 * List item 1
 * List item 2
 ```

 ### Building for Production

 To build your site for GitHub Pages deployment:

 ```bash
 ./build.sh
 ```

 This will generate your site with the correct base path for your GitHub repository.

 ### Base Path Configuration

 For local development, the base path defaults to `/`. For GitHub Pages, you need to set it to your repository name:

 ```bash
 python src/main.py "/YourRepoName/"
 ```

 Or edit the `build.sh` script to include your repository name.

 ## Contributing

 Contributions are welcome! Here's how you can contribute:

 1. Fork the repository
 2. Create a feature branch: `git checkout -b new-feature`
 3. Commit your changes: `git commit -am 'Add new feature'`
 4. Push to the branch: `git push origin new-feature`
 5. Submit a pull request

 Please make sure your code follows the project's style guidelines and includes appropriate tests.