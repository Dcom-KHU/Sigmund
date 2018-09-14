<template>
    <div class="nav-wrapper">
        <div class="icon-container">
            <i class="fas fa-home"></i>
            <i class="fas fa-users"></i>
            <i class="fas fa-home"></i>
        </div>
        <div class="icon-container">
            <i class="fas fa-home" v-on:click="movePage('main')"></i>
            <i class="fas fa-question" v-on:click="movePage('competition')"></i>
            <i class="fas fa-users"></i>
        </div>
        <div class="icon-container">
            <i class="fab fa-twitter"></i>
            <i class="fab fa-facebook-square"></i>
        </div>
    </div>
</template>
<script>
import router from '../../router';

export default {
    methods:{
        movePage(src){  
            router.push({ name : src });
        },
    },
}
</script>
<style scoped>
.nav-wrapper{
    position: fixed;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 50px;
    height: 100vh;
    background-color: #181818;
}
.icon-container{
    display: flex;
    flex-direction: column;
    flex: 1 0 30px;
}
.icon-container > i{
    margin: 5px 0px;
}
.icon-container > i:hover{
    color: #08FDD8;
}
.icon-container:nth-of-type(1){
    margin-top: 16px;
    justify-content: flex-start;
}
.icon-container:nth-of-type(2){
    justify-content: center;
}
.icon-container:nth-of-type(3){
    margin-bottom: 16px;
    justify-content: flex-end;
}
.fas, .fab, .fal{
    display: block;
    color: #585858;
}
</style>
