function setRoutes(app) {
    const AppointmentController = require('../controllers/appointmentController');
    const appointmentController = new AppointmentController();

    app.post('/appointments', appointmentController.createAppointment.bind(appointmentController));
    app.get('/appointments/:id', appointmentController.getAppointment.bind(appointmentController));
    app.put('/appointments/:id', appointmentController.updateAppointment.bind(appointmentController));
    app.delete('/appointments/:id', appointmentController.deleteAppointment.bind(appointmentController));
}

module.exports = setRoutes;