node{
    stage('Preparation') {
        checkout scm
    }
    stage('test') {
        def myTestContainer = docker.image('python:3.12.0a3-bullseye')
        myTestContainer.inside {
            sh 'pip install pipenv'
            sh 'pipenv install'
            sh 'pipenv run python -m pytest'
        }
    }
}
