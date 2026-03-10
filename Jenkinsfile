pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/abhishek00789pandey-alt/Api-automation-framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                bat 'python -m pytest'
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat 'pytest --alluredir=reports'
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