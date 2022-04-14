properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
        git "https://github.com/eyalbit/DevOps2402.git"
    }
    stage("dir"){
        bat "dir"
    }
}
