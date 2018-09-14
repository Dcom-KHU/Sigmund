<template>
    <div id="slide-wrapper">
        <img class="fade-in" src="../../assets/competition1.png">
    </div>
</template>
<script>
export default {

}
</script>
<style scoped>
#slide-wrapper{
    margin: 30px 0px;
}
.fade-in{
    animation-duration: 2s;
    animation-name: fade-in;
    animation-timing-function: ease;
    animation-fill-mode: forwards;
}
.fade-out{
    animation-duration: 2s;
    animation-name: fade-out;
    animation-timing-function: ease;
    animation-fill-mode: forwards;
}
@keyframes fade-out{
    from{
        transform: translateX(0px);
    }
    to{
        transform: translateX(-400px);
    }
}
@keyframes fade-in{
    from{
        transform: translateX(400px);
    }
    to{
        transform: translateX(0px);
    }
}
</style>
