<template>
    <div class="hero has-bg-img is-fullheight ">
        <PresentationTitle class="hero-head "/>
        <Presentation class="hero-body"
                      style="padding: 0 1.5rem;"/>
        <Footer class="hero-foot"/>
    </div>
</template>

<script>
    import PresentationTitle from './components/Header.vue';
    import Presentation from './components/Presentation.vue';
    import Footer from './components/Footer.vue';

    export default {
        name: 'App',
        components: {
            PresentationTitle,
            Presentation,
            Footer,
        },
    };
</script>

<style>
    .has-bg-img {
        background: url("assets/img/background.svg") no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;

    }

</style>
