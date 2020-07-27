"""Generated message classes for edgeml version v1beta1.

Provides ML releated services for Cloud IoT Edge devices
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'edgeml'


class AnalyzeModelRequest(_messages.Message):
  r"""Request for `AnalyzeModel`

  Fields:
    gcsSource: The Google Cloud Storage location of the input.
  """

  gcsSource = _messages.MessageField('GcsSource', 1)


class AnalyzeModelResponse(_messages.Message):
  r"""Response for `AnalyzeModel`. Will be served in
  `google.longrunning.Operation.result.response`

  Enums:
    ModelTypeValueValuesEnum: Model type of the input file.

  Fields:
    additionalMessage: Informative message, if any.
    edgeTpuCompilability: Indicates if the file can be compiled to Edge TPU
      optimized TFLite model file by the latest version Edge TPU compiler.
    modelSignature: The information of input and output vectors of the model,
      if available. Will be set only if model_type is TFLite or TFLite
      optimized for Edge TPU.
    modelType: Model type of the input file.
  """

  class ModelTypeValueValuesEnum(_messages.Enum):
    r"""Model type of the input file.

    Values:
      MODEL_TYPE_UNSPECIFIED: Default: not specified.
      TENSORFLOW_LITE: TensorFlow Lite model (not optimized for Edge TPU).
      TENSORFLOW_LITE_EDGE_TPU_OPTIMIZED: TensorFlow Lite model optimized for
        Edge TPU.
      TENSORFLOW_SAVED_MODEL: TensorFlow SavedModel.
      NON_TENSORFLOW_MODEL: Non-TensorFlow model. Currently, only scikit-learn
        is supported.
      UNKNOWN_FORMAT: Unknown format.
    """
    MODEL_TYPE_UNSPECIFIED = 0
    TENSORFLOW_LITE = 1
    TENSORFLOW_LITE_EDGE_TPU_OPTIMIZED = 2
    TENSORFLOW_SAVED_MODEL = 3
    NON_TENSORFLOW_MODEL = 4
    UNKNOWN_FORMAT = 5

  additionalMessage = _messages.StringField(1)
  edgeTpuCompilability = _messages.MessageField('EdgeTpuCompilability', 2)
  modelSignature = _messages.MessageField('ModelSignature', 3)
  modelType = _messages.EnumField('ModelTypeValueValuesEnum', 4)


class AnalyzeOperationMetadata(_messages.Message):
  r"""Metadata that will be used in google.longrunning.Operation of
  `AnalyzeModel` request. Indicates the current state of the `AnalyzeModel`
  operation.

  Enums:
    StateValueValuesEnum: State of the operation.

  Fields:
    additionalMessage: Informative message, if any.
    elapsedDuration: Indicates how long has been elapsed since the operation
      started, according to the server time.
    startTime: Indicates when the operation started, according to the server
      time.
    state: State of the operation.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""State of the operation.

    Values:
      OPERATION_STATE_UNSPECIFIED: Default: not specified.
      PENDING: In queue, waiting for the process.
      IN_PROGRESS: In progress.
      SUCCEEDED: The operation has been done successfully.
      FAILED: The operation has been failed.
    """
    OPERATION_STATE_UNSPECIFIED = 0
    PENDING = 1
    IN_PROGRESS = 2
    SUCCEEDED = 3
    FAILED = 4

  additionalMessage = _messages.StringField(1)
  elapsedDuration = _messages.StringField(2)
  startTime = _messages.StringField(3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class CompileModelRequest(_messages.Message):
  r"""Request for `CompileModel`. Will be served in
  `google.longrunning.Operation.result.response`

  Enums:
    ChipTypeValueValuesEnum: The target chip type.

  Fields:
    chipType: The target chip type.
    inputConfig: Configuration specifying the input model to compile.
      Currently, only TensorFlow Lite is supported. The requesting user must
      have `read` access to the input location.
    minRuntimeVersion: The required minimum version of Edge TPU runtime. A
      version name such as "1.0.0" or "latest" are allowed.
    outputConfig: Configuration specifying an output location for the compiled
      TensorFlow Lite model. The destination location specified in
      `output_config` must be different from the source location specified in
      `input_config`. The requesting user must have `write` access to the
      output location. If a file exists in the specified path, overwrites to
      that path.
  """

  class ChipTypeValueValuesEnum(_messages.Enum):
    r"""The target chip type.

    Values:
      CHIP_TYPE_UNSPECIFIED: Default: not specified.
      EDGE_TPU_V1: Version 1 of the Edge TPU.
    """
    CHIP_TYPE_UNSPECIFIED = 0
    EDGE_TPU_V1 = 1

  chipType = _messages.EnumField('ChipTypeValueValuesEnum', 1)
  inputConfig = _messages.MessageField('InputConfig', 2)
  minRuntimeVersion = _messages.StringField(3)
  outputConfig = _messages.MessageField('OutputConfig', 4)


class CompileModelResponse(_messages.Message):
  r"""Response for `CompileModel`. Will be served in
  `google.longrunning.Operation.result.response`

  Fields:
    additionalMessage: Additional message, if any. For example, warning
      messages emitted while compiling.
    compileDuration: How long did it take to finish the compilation.
    fileSizeBytes: Size(in bytes) of the compiled file.
    modelSignature: The information of input and output vectors of the
      compiled model.
  """

  additionalMessage = _messages.StringField(1)
  compileDuration = _messages.StringField(2)
  fileSizeBytes = _messages.IntegerField(3)
  modelSignature = _messages.MessageField('ModelSignature', 4)


class CompileOperationMetadata(_messages.Message):
  r"""Metadata that will be used in google.longrunning.Operation of
  `CompileModel` request. Indicates the current state of the `CompileModel`
  operation.

  Enums:
    StateValueValuesEnum: State of the operation.

  Fields:
    additionalMessage: Informative message, e.g. log messages emitted by Edge
      TPU compiler.
    elapsedDuration: Indicates how long has been elapsed since the operation
      started, according to the server time.
    startTime: Indicates when the operation started, according to the server
      time.
    state: State of the operation.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""State of the operation.

    Values:
      OPERATION_STATE_UNSPECIFIED: Default: not specified.
      PENDING: In queue, waiting for the process.
      IN_PROGRESS: In progress.
      SUCCEEDED: The operation has been done successfully.
      FAILED: The operation has been failed.
    """
    OPERATION_STATE_UNSPECIFIED = 0
    PENDING = 1
    IN_PROGRESS = 2
    SUCCEEDED = 3
    FAILED = 4

  additionalMessage = _messages.StringField(1)
  elapsedDuration = _messages.StringField(2)
  startTime = _messages.StringField(3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class ConvertModelRequest(_messages.Message):
  r"""Request for `ConvertModel`.

  Fields:
    inputConfig: Configuration specifying the input model to convert.
      Currently, only TensorFlow SavedModel is supported.
    outputConfig: Configuration specifying an output location for the
      TensorFlow Lite model. The destination location specified in
      `output_config` must be different from the source location specified in
      `input_config`. The requesting user must have `write` access to the
      output location. If a file exists in the specified path, overwrites to
      that path.
    tfliteConverterVersion: The version of TFLite converter to use. A version
      name such as "1.12.0" or "latest" are allowed. Currently, only "1.12.0"
      is supported. If not specified, latest version will be used.
  """

  inputConfig = _messages.MessageField('InputConfig', 1)
  outputConfig = _messages.MessageField('OutputConfig', 2)
  tfliteConverterVersion = _messages.StringField(3)


class ConvertModelResponse(_messages.Message):
  r"""Response for `ConvertModel`.

  Fields:
    additionalMessage: Informative message, if any. For example, it can be
      warning messages from converter.
    convertDuration: How long did it take to finish the conversion
    edgeTpuCompilability: Indicates if the file can be compiled to Edge TPU
      optimized TFLite model file by the latest version Edge TPU compiler.
    fileSizeBytes: Size(in bytes) of the converted file
    modelSignature: The information of input and output vectors of the
      compiled model.
    tfliteConverterVersion: The version of the converter used, e.g. "1.12.0".
      If not specified, latest version will be used.
  """

  additionalMessage = _messages.StringField(1)
  convertDuration = _messages.StringField(2)
  edgeTpuCompilability = _messages.MessageField('EdgeTpuCompilability', 3)
  fileSizeBytes = _messages.IntegerField(4)
  modelSignature = _messages.MessageField('ModelSignature', 5)
  tfliteConverterVersion = _messages.StringField(6)


class ConvertOperationMetadata(_messages.Message):
  r"""Metadata that will be used in google.longrunning.Operation of
  `ConvertModel` request. Indicates the current state of the `ConvertModel`
  operation.

  Enums:
    StateValueValuesEnum: State of the operation.

  Fields:
    additionalMessage: Informative message, if any.
    elapsedDuration: Indicates how long has been elapsed since the operation
      started, according to the server time.
    startTime: Indicates when the operation started, according to the server
      time.
    state: State of the operation.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""State of the operation.

    Values:
      OPERATION_STATE_UNSPECIFIED: Default: not specified.
      PENDING: In queue, waiting for the process.
      IN_PROGRESS: In progress.
      SUCCEEDED: The operation has been done successfully.
      FAILED: The operation has been failed.
    """
    OPERATION_STATE_UNSPECIFIED = 0
    PENDING = 1
    IN_PROGRESS = 2
    SUCCEEDED = 3
    FAILED = 4

  additionalMessage = _messages.StringField(1)
  elapsedDuration = _messages.StringField(2)
  startTime = _messages.StringField(3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class EdgeTpuCompilability(_messages.Message):
  r"""Indicates if the TFLite model can be compiled to Edge TPU optimized
  TFLite model.

  Enums:
    CompilableReasonValueValuesEnum: If set, the model can be compiled. If the
      value is not `COMPILABLE`, compiler might emit an warning message.
    UncompilableReasonValueValuesEnum: If set, the model cannot be compiled.

  Fields:
    additionalMessage: An informative message, if any.
    compilableReason: If set, the model can be compiled. If the value is not
      `COMPILABLE`, compiler might emit an warning message.
    uncompilableReason: If set, the model cannot be compiled.
  """

  class CompilableReasonValueValuesEnum(_messages.Enum):
    r"""If set, the model can be compiled. If the value is not `COMPILABLE`,
    compiler might emit an warning message.

    Values:
      COMPILABLE_REASON_UNSPECIFIED: Default: unspecified
      COMPILABLE: The model can be compiled to Edge TPU optimized TFLite
        model.
      UNVERIFIED_ARCHITECTURE: The model can be compiled to Edge TPU optimized
        TFLite model, but has an unverified architecture. Compiler might emit
        an warning message.
    """
    COMPILABLE_REASON_UNSPECIFIED = 0
    COMPILABLE = 1
    UNVERIFIED_ARCHITECTURE = 2

  class UncompilableReasonValueValuesEnum(_messages.Enum):
    r"""If set, the model cannot be compiled.

    Values:
      UNCOMPILABLE_REASON_UNSPECIFIED: Default: unspecified
      NON_TENSORFLOW_LITE: Only TensorFlow Lite models can be compiled.
      NON_QUANTIZED_MODEL: The model cannot be compiled since it is not
        quantized.
      INPUT_TOO_LARGE: The model cannot be compiled since it is too big.
      ALREADY_COMPILED: The model cannot be compiled since it is already
        compiled.
    """
    UNCOMPILABLE_REASON_UNSPECIFIED = 0
    NON_TENSORFLOW_LITE = 1
    NON_QUANTIZED_MODEL = 2
    INPUT_TOO_LARGE = 3
    ALREADY_COMPILED = 4

  additionalMessage = _messages.StringField(1)
  compilableReason = _messages.EnumField('CompilableReasonValueValuesEnum', 2)
  uncompilableReason = _messages.EnumField('UncompilableReasonValueValuesEnum', 3)


class EdgemlOperationsGetRequest(_messages.Message):
  r"""A EdgemlOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class EdgemlProjectsModelsAnalyzeRequest(_messages.Message):
  r"""A EdgemlProjectsModelsAnalyzeRequest object.

  Fields:
    analyzeModelRequest: A AnalyzeModelRequest resource to be passed as the
      request body.
    project: The project name, e.g. "projects/project_123"
  """

  analyzeModelRequest = _messages.MessageField('AnalyzeModelRequest', 1)
  project = _messages.StringField(2, required=True)


class EdgemlProjectsModelsCompileRequest(_messages.Message):
  r"""A EdgemlProjectsModelsCompileRequest object.

  Fields:
    compileModelRequest: A CompileModelRequest resource to be passed as the
      request body.
    project: The project name, e.g. "projects/project_123"
  """

  compileModelRequest = _messages.MessageField('CompileModelRequest', 1)
  project = _messages.StringField(2, required=True)


class EdgemlProjectsModelsConvertRequest(_messages.Message):
  r"""A EdgemlProjectsModelsConvertRequest object.

  Fields:
    convertModelRequest: A ConvertModelRequest resource to be passed as the
      request body.
    project: The project name, e.g. "projects/project_123"
  """

  convertModelRequest = _messages.MessageField('ConvertModelRequest', 1)
  project = _messages.StringField(2, required=True)


class GcsDestination(_messages.Message):
  r"""The Google Cloud Storage location where the output should be written to.

  Fields:
    outputUri: The Google Cloud Storage URI where the results will be stored.
      Only full object path is accepted, e.g.
      gs://bucket/directory/object.name The result is written to this single
      file.
  """

  outputUri = _messages.StringField(1)


class GcsSource(_messages.Message):
  r"""The Google Cloud Storage location of the input.

  Fields:
    inputUris: Points to [Google Cloud
      Storage](https://cloud.google.com/storage/) URIs containing files with
      input content (only). Only full object path is accepted, e.g.
      gs://bucket/directory/object.name Returns
      [google.rpc.Code.INVALID_ARGUMENT] for all other URI formats.
  """

  inputUris = _messages.StringField(1, repeated=True)


class InputConfig(_messages.Message):
  r"""The input content and metadata.

  Fields:
    gcsSource: The Google Cloud Storage location of the input.
  """

  gcsSource = _messages.MessageField('GcsSource', 1)


class ModelSignature(_messages.Message):
  r"""Describes the signature of a TensorFlow model.

  Fields:
    inputTensors: Info of the input tensors.
    outputTensors: Info of the output tensors.
  """

  inputTensors = _messages.MessageField('TensorRef', 1, repeated=True)
  outputTensors = _messages.MessageField('TensorRef', 2, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OutputConfig(_messages.Message):
  r"""The desired output location and metadata.

  Fields:
    gcsDestination: The Google Cloud Storage location to write the output to.
  """

  gcsDestination = _messages.MessageField('GcsDestination', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class TensorInfo(_messages.Message):
  r"""Information about a tensor.

  Enums:
    InferenceTypeValueValuesEnum: Type of the tensor.

  Fields:
    dimensions: Dimension description of the tensor.
    inferenceType: Type of the tensor.
    tensorName: Name of the tensor.
  """

  class InferenceTypeValueValuesEnum(_messages.Enum):
    r"""Type of the tensor.

    Values:
      INFERENCE_TYPE_UNSPECIFIED: Default: unspecified.
      QUANTIZED_UINT_8: Quantized unsigned 8-bit integer.
      FLOAT_32: 32-bit floating point values.
    """
    INFERENCE_TYPE_UNSPECIFIED = 0
    QUANTIZED_UINT_8 = 1
    FLOAT_32 = 2

  dimensions = _messages.IntegerField(1, repeated=True, variant=_messages.Variant.INT32)
  inferenceType = _messages.EnumField('InferenceTypeValueValuesEnum', 2)
  tensorName = _messages.StringField(3)


class TensorRef(_messages.Message):
  r"""Information about a tensor including its index.

  Fields:
    index: Index of the tensor in the input or output layer.
    tensorInfo: Information about the tensor.
  """

  index = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  tensorInfo = _messages.MessageField('TensorInfo', 2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')