pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                bat '"C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                 bat 'allure generate allure-results --clean -o allure-report'
            }
        }
       stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }
    }
}