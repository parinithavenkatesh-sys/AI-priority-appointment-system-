module.exports = {
    validateAppointmentData: function(data) {
        // Perform validation on appointment data
        if (!data.title || !data.date || !data.time) {
            throw new Error("Missing required appointment fields: title, date, or time.");
        }
        // Additional validation logic can be added here
        return true;
    },

    formatAppointmentDate: function(date) {
        // Format the date to a more readable format
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(date).toLocaleDateString(undefined, options);
    }
};