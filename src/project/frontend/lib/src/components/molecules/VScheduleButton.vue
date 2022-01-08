<template>
<div id="v-schedule-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>Step</p>
          <div><input type="number" v-model="nStep"></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>Sample</p>
          <div><input type="number" v-model="nSample"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Try Scheduling</p>
        </button>
      </div>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.items {
  display: flex;
  align-items: flex-end;
  height: 100px;
}

.item {

  width: 33.3%;

  input {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    box-sizing: border-box;
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
      nStep: 1,
      nSample: 1
    }
  },
  methods: {
    getBestSchedule: function(data) {
      this.$emit("get-best-schedule", data)
    },
    submit: function() {
      this.getBestSchedule({
        n_step: this.nStep,
        n_sample: this.nSample
      })
    }
  }
}
</script>