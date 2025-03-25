<template>
    <div>
      <h2>Vehicle Maintenance</h2>
      <form @submit.prevent="submitForm">
        <label for="mileage">Enter current mileage:</label>
        <input v-model="mileage" id="mileage" type="number" required />
  
        <label for="last_service_date">Enter last service date:</label>
        <input v-model="lastServiceDate" id="last_service_date" type="date" required />
  
        <button type="submit">Submit</button>
      </form>
  
      <div v-if="nextService">
        <h3>Next Service Information:</h3>
        <p>Next Service Due at: {{ nextService.mileage }} miles on {{ nextService.date }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        mileage: '',
        lastServiceDate: '',
        nextService: null,
      };
    },
    methods: {
      async submitForm() {
        try {
          const response = await fetch('http://127.0.0.1:5000/api/calculate', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              mileage: this.mileage,
              last_service_date: this.lastServiceDate,
            }),
          });
  
          if (response.ok) {
            const data = await response.json();
            this.nextService = data; // Store the response
          } else {
            console.error('Failed to fetch data from API');
          }
        } catch (error) {
          console.error('Error submitting form:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  input {
    padding: 8px;
  }
  
  button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  h3 {
    margin-top: 20px;
  }
  </style>
  