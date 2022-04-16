using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class orbitCamera : MonoBehaviour
{

public float turnSpeed =4.0f;
public Transform player;
private Vector3 offset;



void Start () {
    offset = new Vector3( player.position.x, player.position.y+8.0f,player.position.z-15.0f );

}

void LateUpdate () {
    offset = Quaternion.AngleAxis(Input.GetAxis("Mouse X")*turnSpeed,Vector3.up)*offset;
    offset = Quaternion.AngleAxis(Input.GetAxis("Mouse Y")*turnSpeed,Vector3.left)*offset;
    transform.position = player.position+offset;
    transform.LookAt(player.position);
}


} 