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
                    if (response.data == "Error") {
                        alert("User already exists")
                    } else {
                        alert("User created")
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
                }
            }
        }
    }
</script>