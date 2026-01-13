# dhoangquan1.github.io

This is my portfolio website displaying most of my projects, skills, and statuses.

You can develop the local dev environment using Flask, then use Freeze to "squash" the HTMLs file into index.html
The index.html can be used to deploy directly to Github Pages.

This approach helps you avoid the annoying deployment of the app every time you develop codes, and let you see changes live.
The Freeze gives a quick way to deploy your portfolio. The deployable files are located in /docs

------------------------
## ⚙️ Technologies Used
-----------------------
[![My Skills](https://skillicons.dev/icons?i=js,html,css,flask)](https://skillicons.dev)

------------------------
## 🌟 Pages
-----------------------
- **Home**: Home about page
- **Projects**: Display projects in carousel
- **Education**: List degrees, GPAs, and awards
- **Contact**: Extra links and contact information

------------------------
## 🚀 Getting Started
-----------------------

### Set up dependencies:
- Create a python environment:
    ```
    python -m venv venv
    ```
- Activate the python environment:
    ```
    .\venv\Scripts\activate
        or
    source venv/Scripts/activate (for Bash)
    ```
- Download dependencies:
    ```
    pip install -r requirements.txt
    ```

------------------------
## 🖥️ Running the program
-----------------------
### To run this app:
- Start the application with the following command:
    ```
    python app.py
    ```

### To freeze and build the app for deployment:
- Build the application with the following command:
    ```
    python app.py build
    ```
