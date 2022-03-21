from flask import Blueprint, redirect, render_template, request, url_for, flash
from models.cont import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts = contacts)

@contacts.route("/new", methods=['POST'])
def create():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    
    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()
    flash("contacto registrado exitosamente", 'info')
    
    return redirect(url_for('contacts.home'))

@contacts.route("/update/<id>", methods=['POST','GET'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        
        db.session.commit()
        flash("contacto actualizado exitosamente!", 'info')
        return redirect(url_for('contacts.home'))
    else:
        return render_template('create.html', contact=contact)

@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("contacto eliminado exitosamente", 'info')
    return redirect(url_for('contacts.home'))