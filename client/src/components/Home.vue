<template>
    <div>
    {{ data().msg }}
    </div>
</template>

<script>

export default {
    name: 'Home',
    methods: {
        data() {
            return {
                msg: 'Hello World!'
            }
        }
    }
}
</script>