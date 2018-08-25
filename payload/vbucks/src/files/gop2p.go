type Connection struct {

	DestinationNode    *node.Node `json:"destination node"`  // Node to contact

	InitializationNode *node.Node `json:"initializing node"` // Node initializing connection

	Data []byte `json:"data"` // Actual data being transmitted

	Port int `json:"port"`

	ConnectionType  string  `json:"type"` // Type of connection
	ConnectionStack []Event `json:"stack"`
}

type Resolution struct {

	ResolutionData []byte `json:"data"` // ResolutionData - data being passed via resolution (typically a struct)

	GuidingType interface{} `json:"guide"` // GuidingType - guiding struct to map resolution fields
}

func NewConnection(sourceNode *node.Node, destinationNode *node.Node, port int, data []byte, connectionType string, connectionStack []Event) (*Connection, error) {

	if strings.ToLower(connectionType) != "relay" && strings.ToLower(connectionType) != "pointer" { // Check connection type is valid

		return &Connection{}, errors.New("invalid connection type") // Error occurred, return nil

	} else if reflect.ValueOf(destinationNode).IsNil() || reflect.ValueOf(sourceNode).IsNil() { // Check that peer values aren't nil

		return &Connection{}, errors.New("invalid peer value") // Peer values nil, return nil constructor

	} else if len(data) == 0 { // Check that data is being passed trough

		return &Connection{}, errors.New("invalid data") // Return error
	}

	return &Connection{DestinationNode: destinationNode, Port: port, InitializationNode: sourceNode, Data: data, ConnectionType: connectionType, ConnectionStack: connectionStack}, nil // No error occurred, return correctly initialized Connection
}

func NewResolution(data []byte, guidingType interface{}) (*Resolution, error) {

	if len(data) == 0 { // Check for invalid data

		return &Resolution{}, errors.New("nil value found") // Return found error

	}

	return &Resolution{ResolutionData: data, GuidingType: guidingType}, nil // No error occurred, return initialized Resolution
}

func (connection *Connection) Attempt() error {

	if len(connection.ConnectionStack) == 0 { // No connection stack, attempt connection

		return connection.attempt()
	}

	return connection.attemptStack() // Found connection stack, handle respectively
}

func (connection *Connection) attempt() error {

	fmt.Println("-- CONNECTION -- attempting connection")

	serializedConnection, err := common.SerializeToBytes(connection) // Serialize connection

	if err != nil { // Check for errors

		return err // Return found error
	}

	err = common.SendBytes(serializedConnection, connection.DestinationNode.Address+":"+strconv.Itoa(connection.Port)) // Attempt to send event

	if err != nil { // Check for errors

		return err // Return found error
	}

	return nil // No error occurred, return nil
}

func (connection *Connection) attemptStack() error {

	fmt.Println("-- CONNECTION -- attempting stack") // Log connection

	x := 0 // Init iterator

	for x != len(connection.ConnectionStack) { // Iterate through connection stack

		err := connection.ConnectionStack[x].Attempt() // Attempt event

		if err != nil { // Check for errors
		
			return err // Return found error
		}

		x++ // Increment iterator
	}

	return nil // No error occurred, return nil
}
/*
	END EXPORTED METHODS
*/