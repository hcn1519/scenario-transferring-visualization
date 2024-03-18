from enum import Enum
import base64
import math

from protobuf_to_dict import protobuf_to_dict
from cyber_record.record import Record

class CyberRecordReader:

    class TargetChannels(Enum):
        PERCEPTION_OBSTACLES = "/apollo/perception/obstacles"
        ROUTING_REQUEST = "/apollo/routing_request"
        TRAFFIC_LIGHT = "/apollo/perception/traffic_light"
        MONITOR = "/apollo/monitor"
        ROUTING_RESPONSE = "/apollo/routing_response"
        ROUTING_RESPONSE_HISTORY = "/apollo/routing_response_history"
        PLANNING = "/apollo/planning"
        LEARNING_DATA = "/apollo/planning/learning_data"
        PREDICTION = "/apollo/prediction"
        PREDICTION_PERCEPTION_OBSTACLES = "/apollo/prediction/perception_obstacles"
        LOCALIZATION_POSE = "/apollo/localization/pose"
        CANBUS_CHASSIS = "/apollo/canbus/chassis"

    def read_channel(self, source_path: str, channel: TargetChannels, max_count=float('inf')):
        record = Record(source_path)
        messages = record.read_messages(channel.value)
        result = []
        count = 0
        
        for topic, message, t in messages:
            if count > max_count:
                break
            result.append(protobuf_to_dict(message, use_enum_labels=True))
            count += 1

        py_dict = {channel.name: result} # Set channel name as a key to output
        decoded_dict = self.decode_binary(py_dict)

        channel_name = channel.name.lower()
        return (decoded_dict, channel_name, source_path)

    def read_all_channels(self, source_path: str, maxCount=float('inf')):
        """
        Read all target channels
        """
        res = []
        for channel in CyberRecordReader.TargetChannels:
            res.append(self.read_channel(source_path=source_path, channel=channel, maxCount=maxCount))
        return res

    def decode_binary(self, value):
        """
        Recursively decode bytes into utf-8 values
        """
        if isinstance(value, bytes):
            try:
                decoded_value = value.decode("utf-8")
                return decoded_value
            except base64.binascii.Error:
                return value
        elif isinstance(value, list):
            return [self.decode_binary(item) for item in value]
        elif isinstance(value, dict):
            return {
                key: self.decode_binary(sub_value)
                for key, sub_value in value.items()
            }
        elif isinstance(value, float) and math.isnan(value):
            return 0.0
        else:
            return value