pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/api-automation-framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                bat 'pytest'
            }
        }

    }
}