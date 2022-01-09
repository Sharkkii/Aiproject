<template>
<div id="v-model-load-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>agent_name</p>
          <div><input type="text" v-model="name"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Load</p>
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

  width: 50%;

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
  name: "VModelLoadButton",
  data: function() {
    return {
      name: ""
    }
  },
  methods: {
    loadModel: function(data) {
      this.$emit("load-model", data);
    },
    submit: function() {
      this.loadModel({
        name: this.name
      })
    }
  }
}
</script>
