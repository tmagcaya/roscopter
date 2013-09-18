"""autogenerated by genpy from roscopter/Attitude.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Attitude(genpy.Message):
  _md5sum = "a0ed90d05663fe955b3f4e85f83050df"
  _type = "roscopter/Attitude"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#roll                      : Roll angle (rad) (float)     
#pitch                     : Pitch angle (rad) (float) 
#yaw                       : Yaw angle (rad) (float)
#rollspeed                 : Roll angular speed (rad/s) (float)
#pitchspeed                : Pitch angular speed (rad/s) (float)
#yawspeed                  : Yaw angular speed (rad/s) (float)    

float32 roll
float32 pitch
float32 yaw 
float32 rollspeed 
float32 pitchspeed
float32 yawspeed

"""
  __slots__ = ['roll','pitch','yaw','rollspeed','pitchspeed','yawspeed']
  _slot_types = ['float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       roll,pitch,yaw,rollspeed,pitchspeed,yawspeed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Attitude, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.rollspeed is None:
        self.rollspeed = 0.
      if self.pitchspeed is None:
        self.pitchspeed = 0.
      if self.yawspeed is None:
        self.yawspeed = 0.
    else:
      self.roll = 0.
      self.pitch = 0.
      self.yaw = 0.
      self.rollspeed = 0.
      self.pitchspeed = 0.
      self.yawspeed = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.roll, _x.pitch, _x.yaw, _x.rollspeed, _x.pitchspeed, _x.yawspeed))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.roll, _x.pitch, _x.yaw, _x.rollspeed, _x.pitchspeed, _x.yawspeed,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.roll, _x.pitch, _x.yaw, _x.rollspeed, _x.pitchspeed, _x.yawspeed))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.roll, _x.pitch, _x.yaw, _x.rollspeed, _x.pitchspeed, _x.yawspeed,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6f = struct.Struct("<6f")