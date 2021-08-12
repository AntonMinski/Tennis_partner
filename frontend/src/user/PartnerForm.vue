<template>
    <form @submit.prevent="submitForm">
        <div class="form-control" :class="{invalid: !firstName.isvalid}">
            <label for="firstName">First name:</label>
            <input type="text" id="firstName" v-model.trim="firstName.val"
            @blur="clearValidity('firstName')" />
            <p v-if="!firstName.isvalid">First name should not be empty</p>
        </div>
        <div class="form-control" :class="{invalid: !lastName.isvalid}">
            <label for="lastName">Last name:</label>
            <input type="text" id="lastName" v-model.trim="lastName.val"
            @blur="clearValidity('lastName')" />
            <p v-if="!lastName.isvalid">Last name should not be empty</p>
        </div>
        <div class="form-control" :class="{invalid: !age.isvalid}">
            <label for="age">Age:</label>
            <input type="number" id="age" v-model.number="age.val"
                   @blur="clearValidity('age')"
            />
            <p v-if="!age.isvalid">Age can't be null</p>
        </div>
        <div class="form-control" :class="{invalid: !description.isvalid}">
            <label for="description">Describe yourself:</label>
            <textarea id="description" rows="5" v-model.trim="description.val"
            @blur="clearValidity('description')" />
            <p v-if="!description.isvalid">Description name should not be empty</p>
        </div>
        <div class="form-control" :class="{invalid: !skillLevel.isvalid}">
            <label for="skillLevel">Your skills level by NTRP:</label>
            <input type="number" id="skillLevel" v-model.number="skillLevel.val"
            @blur="clearValidity('skillLevel')" />
            <p v-if="!skillLevel.isvalid">Skills level should be greater than 0</p>
        </div>
        <div class="form-control" :class="{invalid: !sportStyles.isvalid}">
            <h3>Sport styles you can play:</h3>
            <div>
                <input type="checkbox" id="football" value="football"
                       v-model="sportStyles.val" >
                <label for="football">Football</label>
            </div>
            <div>
                <input type="checkbox" id="tennis" value="tennis"
                 v-model="sportStyles.val" >
                <label for="tennis">Tennis</label>
            </div>
            <div>
                <input type="checkbox" id="bike" value="bike"
                 v-model="sportStyles.val" >
                <label for="bike">Bike trips / races / enduro</label>
            </div>
            <p v-if="!sportStyles.isvalid">Select at least 1</p>
        </div>
        <p v-if="!formIsValid">Please fix the above errors and submit again</p>
        <basic-button>Register</basic-button>
    </form>
</template>

<script>
    // import BasicButton from "../ui/BasicButton";

    export default {
        // components: {BasicButton},
        emits: ['save-data'],
        data() {
            return {
                firstName: {
                    val: '',
                    isvalid: true
                },
                lastName: {
                    val: '',
                    isvalid: true
                },
                age: {
                    val: null,
                    isvalid: true
                },
                description: {
                    val: '',
                    isvalid: true
                },
                skillLevel: {
                    val: null,
                    isvalid: true
                },
                sportStyles: {
                    val: [],
                    isvalid: true
                },
                formIsValid: true,
            };
        },
        methods: {
            clearValidity(input) {
                this.[input].isvalid = true;


            },
            validateForm() {
                this.formIsValid = true;
                if (this.firstName.val === '') {
                    this.firstName.isvalid = false;
                    this.formIsValid = false;
                }
                if (this.lastName.val === '') {
                    this.lastName.isvalid = false;
                    this.formIsValid = false;
                }
                if (!this.age.val) {
                    this.age.isvalid = false;
                    this.formIsValid = false;
                }
                if (this.description.val === '') {
                    this.description.isvalid = false;
                    this.formIsValid = false;
                }
                if (!this.skillLevel.val || this.skillLevel.val <0) {
                    this.skillLevel.isvalid = false;
                    this.formIsValid = false;
                }
                if (this.sportStyles.val.length === 0) {
                    this.sportStyles.isvalid = false;
                    this.formIsValid = false;
                }

            },
            submitForm() {
                this.validateForm();

                if (!this.formIsValid) {
                    return;
                }

                const formData = {
                    first: this.firstName.val,
                    last: this.lastName.val,
                    age: this.age.val,
                    desc: this.description.val,
                    lvl: this.skillLevel.val,
                    stl: this.sportStyles.val,
                };

                this.$emit('save-data', formData);
            },
        },

    };
</script>

<style scoped>
.form-control {
  margin: 0.5rem 0;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input[type="checkbox"] + label {
  font-weight: normal;
  display: inline;
  margin: 0 0 0 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  border: 1px solid #ccc;
  font: inherit;
}

input:focus,
textarea:focus {
  background-color: #f8fceb;
  outline: none;
  border-color: #3d008d;
}

input[type="checkbox"] {
  display: inline;
  width: auto;
  border: none;
}

input[type="checkbox"]:focus {
  outline: #898989 solid 1px;
}

h3 {
  margin: 0.5rem 0;
  font-size: 1rem;
}

.invalid label {
  color: red;
}

.invalid input,
.invalid textarea {
  border: 1px solid red;
}
</style>