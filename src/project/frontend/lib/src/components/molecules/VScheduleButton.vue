<template>
<div id="v-schedule-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="item">
      <label>
        <p>Step</p>
        <div><input type="number" v-model="nStep"></div>
      </label>
    </div>
    <div class="item">
      <button type="submit">
        <p>Try Job-Scheduling</p>
      </button>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.item {
  margin-top: 10px;

  input {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }
}
</style>

<script>
export default {
  name: "VScheduleButton",
  data: function() {
    return {
      nStep: 1
    }
  },
  methods: {
    scheduleJob: function(data) {
      this.$emit("schedule-job", data)
    },
    submit: function() {
      this.scheduleJob({
        n_step: this.nStep
      })
    }
  }
}
</script>