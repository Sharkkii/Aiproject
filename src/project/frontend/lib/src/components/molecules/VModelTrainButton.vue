<template>
<div id="v-model-train-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>n_epoch</p>
          <div><input type="text" v-model="nEpoch"></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>n_train_eval</p>
          <div><input type="text" v-model="nTrainEval"></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>n_test_eval</p>
          <div><input type="text" v-model="nTestEval"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Train Model</p>
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

  width: 25%;

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
  name: "VModelTrainButton",
  data: function() {
    return {
      nEpoch: 100,
      nTrainEval: 5,
      nTestEval: 5
    }
  },
  methods: {
    trainModel: function(data) {
      this.$emit("train-model", data);
    },
    submit: function() {
      this.trainModel({
        n_epoch: this.nEpoch,
        n_train_eval: this.nTrainEval,
        n_test_eval: this.nTestEval
      })
    }
  }
}
</script>
