def credentials = [
    login: '',
    password: ''
]

pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER_VERSION', choices: ['122.0', '125.0'], description: 'Выберите версию браузера')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                withEnv(["LOGIN=${credentials.login}", "PASSWORD=${credentials.password}"]) {
                    sh """
                        pip install -r requirements.txt
                        pytest tests/test_main_page.py --browser_version=${params.BROWSER_VERSION}
                    """
                }
            }
        }
    }

    post {
        always {
            script {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])

                def message = "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n"
                message += "Подробности: ${env.BUILD_URL}"

                telegramSend(message: message)
            }
        }
    }
}