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
                var login = document.getElementById("login").value;
                var password = document.getElementById("password").value;
                var array = [];
                axios.get("http://localhost:5000/api/login")
                .then(response => { 
                    array[0] = response.data.login; 
                    array[1] = response.data.password;
                    console.log(array);
                    if (login == array[0] && password == array[1])
                    {
                        alert("Login Success");
                    } else {
                        alert("Login Failed");
                    }    
                })
                    .catch(error => { console.log(error); });
                
            },
            alert(message) {
                alert(message);
            },
            signup() {
                var array = [document.getElementById("login").value, document.getElementById("password").value];
                axios.post("http://localhost:5000/api/signup", {login: array[0], password: array[1]});
            }
        }
    }
</script>