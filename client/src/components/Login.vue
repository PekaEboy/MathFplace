<template>
    <div>
        login
        <input id="login"><br>
        password
        <input id="password"><br>
        <button v-on:click="login()">Enter</button>
        <button v-on:click="signup()">Sign Up</button>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Login",
        methods: {
            login() {
                
                axios.get("http://localhost:5000/api/login")
                .then(r => { 
    let adjj = r.data.loginandpassword;
    let avv = []
    let avb = []
    for(let i = 0; i<adjj.length; i++) {
        avv[i]=adjj[i][0]
        avb[i]=adjj[i][1]
    }
    
    let loga=document.getElementById("login").value
    let passw=document.getElementById("password").value
    let pope = 0
    for(let i = 0; i<adjj.length; i++) {
      if (avv[i]==loga && avb[i]==passw ) {
        alert("You have arrived!")
        break
      }
      pope=pope+1
    }
    if (pope==adjj.length) {
      alert("Incorrect login or password")
    }
                })
                    .catch(error => { console.log(error); });
                
            },
            signup() {
                let logininput = document.getElementById("login").value
                /*axios.get("http://localhost:5000/api/login").then(r => {
                    let adj = r.data.loginandpassword;
                    let lgs = []
                    for (let i = 0; i < adj.length; i++) {
                        lgs[i] = adj[i][0]
                    }
                    if (lgs.includes(logininput)) {
                        alert("Login already taken")
                    }
                }).catch(error => { console.log(error); });*/
                let passwordinput = document.getElementById("password").value
                if (logininput.length == 0 || passwordinput.length == 0 || logininput.length > 24 || passwordinput.length > 24 ) {  
                    alert("Please don't write more than 24 characters or null")
                } else {
                    
                    var array = [document.getElementById("login").value, document.getElementById("password").value];
                    axios.post('http://localhost:5000/api/signup', {
                    login: array[0], 
                    password: array[1]
                })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
                alert("You have successfully signed up!")
                }
            }
        }
    }
</script>