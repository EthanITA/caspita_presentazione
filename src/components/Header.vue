<template>
  <b-navbar style="padding-top: 0.5rem; padding-left: 5rem; padding-right: 2rem
">

    <template #brand>
      <b-navbar-item>
        <div class="image is-128x128-real">
          <img
              style="max-height: 100%"
              src="../assets/img/fading_logo.png"
              alt="logo"
          />
        </div>
      </b-navbar-item>
    </template>
    <template #start>

      <b-navbar-item>
        <div class="title is-1 is-uppercase">
          Offerte del giorno
        </div>
      </b-navbar-item>
    </template>
    <template #end>
      <b-navbar-item>
        <div class="subtitle columns is-vcentered has-text-centered">
          <div class="is-5 column ">
            <div class="subtitle is-4">{{ time }},</div>
          </div>
          <div class="is-6 column">
            <div class="subtitle is-5">{{ date }}</div>
          </div>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: 'Title',
  data: () => ({
    time: '',
    mylocale: 'it-IT',
    date: ""
  }),
  methods: {
    getNow: function () {
      const today = new Date();
      this.time = today.toLocaleTimeString(this.mylocale);
      this.date = today.toLocaleString(this.mylocale,
          {
            weekday: 'long',
            day: '2-digit',
            month: 'long',
            year: 'numeric'
          });
    }
  },
  created: function () {
    setInterval(this.getNow, 500);
  }

};
</script>

<style scoped>
.column {
  padding: 0;
}

.is-128x128-real {
  width: 256px;
  height: 128px;
}
</style>
