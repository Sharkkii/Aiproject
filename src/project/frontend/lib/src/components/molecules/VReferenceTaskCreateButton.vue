<template>
<div id="v-reference-task-create-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="item">
      <label>
        <p>Task Name</p>
        <div><input type="text" v-model="name"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Slot</p>
        <div><input type="number" v-model="slot"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Required Effort</p>
        <div><input type="number" v-model="requiredEffort"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Remaining Time</p>
        <div><input type="number" v-model="remainingTime"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>P</p>
        <div><input type="number" step="0.01" v-model="P"></div>
      </label>
    </div>
    <div class="item">
      <button type="submit">
        <p>Create</p>
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
  name: "VReferenceTaskCreateButton",
  data: function() {
    return {
      name: null,
      slot: null,
      requiredEffort: null,
      remainingTime: null,
      P: null
    }
  },
  methods: {
    createReferenceTask: function(data) {
      this.$emit("create-reference-task", data)
    },
    submit: function() {
      this.createReferenceTask({
        name: this.name,
        slot: this.slot,
        remaining_time: this.remainingTime,
        required_effort: this.requiredEffort,
        P: this.P
      })
    }
  }
}
</script>