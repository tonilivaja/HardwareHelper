from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import TestPC, Platform, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	test_pc_list = TestPC.query.all()
	platform_list = Platform.query.all()

	return render_template("home.html", user=current_user, test_pc_list=test_pc_list, platform_list=platform_list)

@views.route('/configure-pcs', methods=['GET', 'POST'])
@login_required
def configure_test_pcs():
	if request.method == 'POST':
		test_pc = request.form.get('testPc')
		ip_address = request.form.get('ipAddress')
		status = "Free"

		if len(test_pc) < 1:
			flash('Test PC name is too short!', category='error')
		elif len(ip_address) > 15:
			flash('IP address is too long!', category='error')
		else:
			new_test_pc = TestPC(name=test_pc, ip_address=ip_address, status=status)
			db.session.add(new_test_pc)
			db.session.commit()
			flash('TestPC added!', category='success')

	test_pc_list = TestPC.query.all()
	return render_template("configure_pcs.html", user=current_user, test_pc_list=test_pc_list)

@views.route('/configure-platforms', methods=['GET', 'POST'])
@login_required
def configure_platforms():
	if request.method == 'POST':
		platform = request.form.get('platform')
		ip_address = request.form.get('ipAddress')
		status = "Free"

		if len(platform) < 1:
			flash('Platform name is too short!', category='error')
		elif len(ip_address) > 15:
			flash('IP address is too long!', category='error')
		else:
			new_platform = Platform(name=platform, ip_address=ip_address, status=status)
			db.session.add(new_platform)
			db.session.commit()
			flash('Platform added!', category='success')

	platform_list = Platform.query.all()
	return render_template("configure_platforms.html", user=current_user, test_pc_list=platform_list)

@views.route('/reserve-test-pc', methods=['GET', 'POST'])
@login_required
def reserve_test_pc():
	test_pc_id = request.form.get('testPcId')
	user_id = request.form.get('userId')

	test_pc = TestPC.query.get(test_pc_id)
	user = User.query.get(user_id)

	test_pc.status = user.user_name
	db.session.commit()

	return redirect('/')

@views.route('/free-pc', methods=['GET', 'POST'])
@login_required
def free_test_pc():
	test_pc_id = request.form.get('testPcId')
	test_pc = TestPC.query.get(test_pc_id)

	test_pc.status = "Free"
	db.session.commit()

	return redirect('/')

@views.route('/delete-test-pc', methods=['POST'])
def delete_test_pc():
	test_pc = json.loads(request.data)
	testPcId = test_pc['testPcId']
	test_pc = TestPC.query.get(testPcId)
	if test_pc:
		db.session.delete(test_pc)
		db.session.commit()
		return jsonify({})

@views.route('/reserve-platform', methods=['GET', 'POST'])
@login_required
def reserve_platform():
	platform_id = request.form.get('platformId')
	user_id = request.form.get('userId')

	platform = Platform.query.get(platform_id)
	user = User.query.get(user_id)

	platform.status = user.user_name
	db.session.commit()

	return redirect('/')

@views.route('/free-platform', methods=['GET', 'POST'])
@login_required
def free_platform():
	platform_id = request.form.get('platformId')
	platform = Platform.query.get(platform_id)

	platform.status = "Free"
	db.session.commit()

	return redirect('/')

@views.route('/delete-platform', methods=['POST'])
def delete_platform():
	platform = json.loads(request.data)
	platformId = platform['platformId']
	platform = Platform.query.get(platformId)
	if platform:
		db.session.delete(platform)
		db.session.commit()
		return jsonify({})