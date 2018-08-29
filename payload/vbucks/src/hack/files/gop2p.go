type Connection struct {

	DestinationNode    *node.Node
	
	`json:"destination node"`  // Node to contact

	InitializationNode *node.Node
	
	`json:"initializing node"` // Node initializing

	Data []byte `json:"data"`

	Port int `json:"port"`

	ConnectionType  string  `json:"type"`
	
	// Connection Type
	
	ConnectionStack []Event `json:"stack"`
}

type Resolution struct {

	ResolutionData []byte `json:"data"`

	GuidingType interface{} `json:"guide"`
}

func NewConnection(sourceNode *node.Node, destinationNode

*node.Node, port int, data []byte, connectionType string,

connectionStack []Event) (*Connection, error) {

	if strings.ToLower(connectionType) != "relay"
	
	&& strings.ToLower(connectionType) != "pointer" {

		return &Connection{},

		errors.New("invalid connection type")

	} else if reflect.ValueOf(destinationNode).IsNil() ||
	
	reflect.ValueOf(sourceNode).IsNil() {

		return &Connection{},
		
		errors.New("invalid peer value")

	} else if len(data) == 0 {

		return &Connection{}, errors.New("invalid data")
	}

	return &Connection{DestinationNode: destinationNode,
	
	Port: port, InitializationNode: sourceNode,
	
	Data: data, ConnectionType: connectionType,
	
	ConnectionStack: connectionStack}, nil
}

func NewResolution(data []byte, guidingType interface{})

(*Resolution, error) {

	if len(data) == 0 { // Check for invalid data

		return &Resolution{},
		
		errors.New("nil value found")

	}

	return &Resolution{ResolutionData: data,
	
	GuidingType: guidingType}, nil
}

func (connection *Connection) Attempt() error {

	if len(connection.ConnectionStack) == 0 {

		return connection.attempt()
	}

	return connection.attemptStack()
}

func (connection *Connection) attempt() error {

	fmt.Println("-- CONNECTION -- attempting connection")

	serializedConnection, err :=
	
	common.SerializeToBytes(connection) // SERIALIZATION

	if err != nil { // Check for errors

		return err // Return found error
	}

	err = common.SendBytes(serializedConnection,
	
	connection.DestinationNode.Address+":" + 
	
	strconv.Itoa(connection.Port))

	if err != nil { // Check for errors

		return err // Return found error
	}

	return nil // No error occurred, return nil
}

func (connection *Connection) attemptStack() error {

	fmt.Println("-- CONNECTION -- attempting stack")

	x := 0 // Init iterator

	for x != len(connection.ConnectionStack) {

		err := connection.ConnectionStack[x].Attempt()

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