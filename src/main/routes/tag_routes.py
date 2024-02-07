from flask import Blueprint, jsonify
tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    return jsonify({"resp": "ok"}), 200
