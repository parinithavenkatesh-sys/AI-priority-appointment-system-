class AppointmentController {
    constructor() {
        this.appointments = [];
    }

    createAppointment(req, res) {
        const appointment = req.body;
        this.appointments.push(appointment);
        res.status(201).json({ message: 'Appointment created', appointment });
    }

    updateAppointment(req, res) {
        const { id } = req.params;
        const updatedData = req.body;
        const appointmentIndex = this.appointments.findIndex(app => app.id === id);

        if (appointmentIndex !== -1) {
            this.appointments[appointmentIndex] = { ...this.appointments[appointmentIndex], ...updatedData };
            res.json({ message: 'Appointment updated', appointment: this.appointments[appointmentIndex] });
        } else {
            res.status(404).json({ message: 'Appointment not found' });
        }
    }

    deleteAppointment(req, res) {
        const { id } = req.params;
        const appointmentIndex = this.appointments.findIndex(app => app.id === id);

        if (appointmentIndex !== -1) {
            this.appointments.splice(appointmentIndex, 1);
            res.json({ message: 'Appointment deleted' });
        } else {
            res.status(404).json({ message: 'Appointment not found' });
        }
    }

    getAppointments(req, res) {
        res.json(this.appointments);
    }
}

export default AppointmentController;