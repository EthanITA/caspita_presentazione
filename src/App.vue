<template>
  <div class="hero has-bg-img ">
    <PresentationTitle class="hero-head"/>
    <Presentation :interval="slide_autoplay_interval" class="hero-body"
                  style="padding: 0 1.5rem;"/>
    <Footer :presentation_interval="slide_autoplay_interval" class="hero-foot"/>
  </div>
</template>

<script>
import PresentationTitle from './components/Header.vue';
import Presentation from './components/Presentation.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  data() {
    return {
      slide_autoplay_interval: 10
    }
  },
  components: {
    PresentationTitle,
    Presentation,
    Footer,
  },
};
</script>

<style>
.hero {
  height: 100vh;
  max-height: 100vh;
}

.has-bg-img {
  background: url("assets/img/background.svg") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;

}

</style>
