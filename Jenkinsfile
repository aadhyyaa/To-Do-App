pipeline {
    agent any
    environment {
        Docker_image = 'to-do-app:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aadhyyaa/To-Do-App.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${Docker_image}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${Docker_image}").inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        if [ "$(docker ps -a -q -f name=PythonContainer2)" ]; then
                            docker stop PythonContainer2
                            docker rm PythonContainer2
                        fi
                        docker run -d -p 5000:5000 --name PythonContainer2 ${Docker_image}
                    '''
                }
            }
        }
    }
}
