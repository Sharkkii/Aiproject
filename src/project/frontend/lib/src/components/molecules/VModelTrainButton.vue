<template>
<div id="v-model-train-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>n_total_epoch</p>
          <div><input type="number" v-model="nTotalEpoch" disabled></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>n_epoch</p>
          <div><input type="number" v-model="nEpoch"></div>
        </label>
      </div>
      <div class="item">
        <label>
          <p>n_eval</p>
          <div><input type="number" v-model="nEval"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit" v-bind:disabled="disabled">
          <p>Train</p>
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
      nTotalEpoch: null,
      nEpoch: null,
      nEval: null,
      disabled: true
    }
  },
  props: {
    status: {
      type: String,
      default: "NG"
    }
  },
  methods: {
    trainModel: function(data) {
      this.$emit("train-model", data);
    },
    submit: function() {
      this.trainModel({
        n_epoch: this.nEpoch,
        n_train_eval: this.nEval,
        n_test_eval: this.nEval
      })
    }
  },
  watch: {
    status: function() {
      if (this.status == "OK") {
        this.disabled = false
      } else if (this.status == "NG") {
        this.disabled = true
      }
    }
  }
}
</script>
