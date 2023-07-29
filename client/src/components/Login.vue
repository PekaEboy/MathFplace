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
                axios.post('http://localhost:5000/api/login', {
                                    login: document.getElementById('login').value,
                                    password: document.getElementById('password').value
                                })
                                  .then(r => {
                                        if (r.data == "Good") {
                                            this.$router.push('/home');
                                        } else {
                                            alert("Unknown login or password!");
                                        }
                                    })
                                  .catch(error => {
                                        console.log(error);
                                    });
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