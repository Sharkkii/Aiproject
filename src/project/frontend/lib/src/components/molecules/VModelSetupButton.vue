<template>
<div id="v-model-setup-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>n_slot</p>
          <div><input type="text" v-model="configuration.nSlot"></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>n_worker</p>
          <div><input type="text" v-model="configuration.nWorker"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Setup Model</p>
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
  name: "VModelSetupButton",
  data: function() {
    return {
      configuration: {
        "nSlot": 5,
        "nWorker": 1
      }
    }
  },
  methods: {
    setupModel: function(data) {
      this.$emit("setup-model", data);
    },
    submit: function() {
      this.setupModel({
        configuration: this.configuration
      })
    }
  }
}
</script>
