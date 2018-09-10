<template>
    <div class="wrapper">
        <Navigation></Navigation>
        <Footer></Footer>
    </div>
</template>
<script>
import Navigation from './Navigation'
import Footer from './Footer'

export default {
    components: {Navigation, Footer},
}
</script>
<style scoped>
.wrapper{
    background-color: #252627;
}
</style>